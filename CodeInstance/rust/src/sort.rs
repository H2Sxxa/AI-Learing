pub type V = Vec<i32>;
/// 选择排序
/// 逐一检索第 i 小的数并交换
pub fn selection_sort(target: &mut V) {
    let max_index = target.len() - 1;
    for i in 0..max_index {
        //无需遍历到 max_index，因为 i = max_index - 1 时候列表已排好序
        let mut ith = i;
        for j in i + 1..=max_index {
            //寻找 i ~ max_index 之间的最小值，需要遍历每一个数字
            if target[j] < target[ith] {
                ith = j;
            }
        }
        target.swap(i, ith);
    }
}

pub fn bubble_sort(target: &mut V) {
    let max_index = target.len() - 1;
    let mut flag = true;
    while flag {
        flag = false;
        // 遍历交换
        for i in 0..max_index - 1 {
            if target[i] > target[i + 1] {
                target.swap(i, i + 1);
                flag = true;
            }
        }
    }
}

#[cfg(test)]
mod sort {
    use super::*;
    #[test]
    fn test_selection_sort() {
        let mut test_v: V = vec![9, 12, 3, 8, 12, 5, 90];
        selection_sort(&mut test_v);
        assert_eq!(test_v, vec![3, 5, 8, 9, 12, 12, 90]);
        println!("Selection Sort -> {:?}", test_v)
    }

    #[test]
    fn test_bubble_sort() {
        let mut test_v: V = vec![9, 12, 3, 8, 12, 5, 90];
        bubble_sort(&mut test_v);
        //assert_eq!(test_v, vec![3, 5, 8, 9, 12, 12, 90]);
        println!("Bubble Sort -> {:?}", test_v)
    }

    #[test]
    fn test_insertion_sort() {
        //let mut test_v: V = vec![9, 12, 3, 8, 12, 5, 90];
        //assert_eq!(test_v, vec![3, 5, 8, 9, 12, 12, 90]);
        //println!("Insertion Sort -> {:?}", test_v)
    }

    #[test]
    fn misc_test() {
        println!("{}", ((((7_f64 / 3_f64) * 10_f64) as i32) as f64) / 10_f64)
    }
}
